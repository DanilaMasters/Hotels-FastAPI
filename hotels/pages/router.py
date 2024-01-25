from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from hotels.hotels.dao import HotelDAO

from hotels.hotels.models import Hotels
from hotels.hotels.router import hotels


router = APIRouter(prefix='/pages', tags=['Pages'])

templates = Jinja2Templates(directory='hotels/templates', )

@router.get('/')
def get_hotels_page(
    request: Request,
    hotels: list[Hotels] = Depends(hotels)
):
    return templates.TemplateResponse(request, 'home.html', context={'hotels': hotels})