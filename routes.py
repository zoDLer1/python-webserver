from src.routing import Router
from src.data_handlers.response import FileResponse, RedirectResponse
from settings import PUBLIC_DIR
from controllers.main_controller import MainController

router = Router()

router.register('/album', 'GET', MainController.as_view())

router.register('/redirect', 'GET', lambda r: RedirectResponse(r, '/album'))

router.use_static(PUBLIC_DIR)
