from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from model import Todo, TodoItem, TodoItems
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.responses import Response

todo_router = APIRouter()
todo_list: list = []
templates = Jinja2Templates(directory="templates/")


@todo_router.get('/todo', response_model=TodoItems)
async def retrive_todo(request: Request) -> Response:
    return templates.TemplateResponse(
        "todo.html",
        {
            "request": request,
            "todos": todo_list   
        } 
    )


@todo_router.get('/todo/{todo_id}')  # todo_id параметр пути
async def get_single_todo(
    request: Request,
    todo_id: int = Path(..., title='The ID of the todo to retrieve.')
) -> Response:
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse(
                "todo.html",
                {
                    "request": request,
                    "todo": todo
                }
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist."
    )


@todo_router.post('/todo', status_code=201)
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)) -> Response:
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return RedirectResponse(url='/todo', status_code=303)
    # return templates.TemplateResponse(
    #     "todo.html",
    #     {
    #         "request": request,
    #         "todos": todo_list
    #     }
    # )


@todo_router.put('/todo/{todo_id}')
async def update_todo(
    todo_data: TodoItem,
    todo_id: int = Path(..., title="The ID of the todo to be updated")
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Todo updated successfully"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist."
    )


@todo_router.delete('/todo/{todo_id}')
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo_id == todo.id:
            todo_list.pop(index)
            return {
                'message': 'Todo deleted successfully'
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist."
    )


@todo_router.delete('/todo')
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        'message': 'Todos deleted successfully'
    }
