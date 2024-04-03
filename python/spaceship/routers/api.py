from fastapi import APIRouter
import numpy

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}


@router.get("/multiply-matrices")
async def multiply_matrices():
    matrixA = numpy.random.rand(10, 10)
    matrixB = numpy.random.rand(10, 10)

    product = numpy.dot(matrixA, matrixB)

    return {
        "matrixA": matrixA.tolist(),
        "matrixB": matrixB.tolist(),
        "product": product.tolist(),
    }