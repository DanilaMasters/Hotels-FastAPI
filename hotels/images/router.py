import shutil
from fastapi import APIRouter, UploadFile

router = APIRouter(prefix='/images', tags=['Pictures'])

@router.post('/hotels')
async def add_hotel_image(id: int, file: UploadFile):
    with open(f'hotels/static/images/{id}.webp', 'wb+') as file_object:
        shutil.copyfileobj(file.file, file_object)