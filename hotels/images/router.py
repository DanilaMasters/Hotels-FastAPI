import shutil
from fastapi import APIRouter, UploadFile

from hotels.tasks.tasks import process_pic

router = APIRouter(prefix='/images', tags=['Pictures'])

@router.post('/hotels')
async def add_hotel_image(id: int, file: UploadFile):
    path = f'hotels/static/images/{id}.webp'
    with open(path, 'wb+') as file_object:
        shutil.copyfileobj(file.file, file_object)
    process_pic.delay(path)