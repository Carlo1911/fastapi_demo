from fastapi import APIRouter, status

from app.models.products import Product
import app.schemas as schemas

router = APIRouter()


@router.get("/", response_model=list[schemas.Product])
async def read_products():
    return await Product.objects.all()


@router.post(
    "/",
    response_model=schemas.Product,
    summary="Crear un producto",
    status_code=status.HTTP_201_CREATED,
)
async def create_product(product: schemas.CreateProduct):
    return await Product.objects.create(**product.dict())

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(id: int):
    return await Product.objects.delete(id=id)
