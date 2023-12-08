import pathlib
from collections.abc import Iterable, Sequence

import cv2
import numpy


def collection(files: Iterable[str | pathlib.Path | bytes], obtained: Sequence[int] | set[int]) -> bytes:
    interrogation_image = pathlib.Path('images/interrogation.png').read_bytes()

    files = list(files)
    size = get_size(files[0])
    if size != (475, 475):
        interrogation_image = resize(interrogation_image, size)

    return concatenate(
        (file if i in obtained else interrogation_image for i, file in enumerate(files, start=1)),
        images_per_line=14
    )


def concatenate(
    files: Iterable[str | pathlib.Path | bytes],
    images_per_line,
    resize_to: tuple[int, int] = None
) -> bytes:
    if resize_to:
        def resize_image(image_: numpy.ndarray, resize_to_: tuple[int, int]) -> numpy.ndarray:
            return cv2.resize(image_, resize_to_, interpolation=cv2.INTER_AREA)
    else:
        def resize_image(image_: numpy.ndarray, _) -> numpy.ndarray:
            return image_

    column_images = []
    row_images = []
    for i, file in enumerate(files, start=1):
        column_images.append(resize_image(to_numpy_array(file), resize_to))
        if i % images_per_line == 0:
            row_images.append(cv2.hconcat(column_images))
            column_images.clear()

    if column_images:
        last_row_image = cv2.hconcat(column_images)
        last_row_image = cv2.copyMakeBorder(last_row_image, 0, 0, 0, (images_per_line - len(column_images)) * last_row_image.shape[0], cv2.BORDER_CONSTANT)
        row_images.append(last_row_image)
    final_image = cv2.vconcat(row_images)
    return cv2.imencode('.png', final_image, [cv2.IMWRITE_PNG_COMPRESSION, 3])[1].tostring()


def get_size(file: str | pathlib.Path | bytes) -> tuple[int, int]:
    image = to_numpy_array(file)
    return image.shape[0], image.shape[1]


def resize(file: str | pathlib.Path | bytes, resize_to: tuple[int, int]) -> bytes:
    resized_image = cv2.resize(to_numpy_array(file), resize_to, interpolation=cv2.INTER_AREA)
    return cv2.imencode('.png', resized_image)[1].tostring()


def to_numpy_array(file: str | pathlib.Path | bytes, ) -> numpy.ndarray:
    if isinstance(file, str):
        return cv2.imread(file, cv2.IMREAD_UNCHANGED)
    elif isinstance(file, pathlib.Path):
        return cv2.imread(str(file), cv2.IMREAD_UNCHANGED)
    else:
        # noinspection PyArgumentList
        array = numpy.fromstring(file, numpy.uint8)
        return cv2.imdecode(array, cv2.IMREAD_UNCHANGED)
