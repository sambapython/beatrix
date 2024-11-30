from fastapi.responses import JSONResponse
def python_exception_handler(exception):
    return JSONResponse(status_code=418, content={"message": exception.args[0]})