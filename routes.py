from src.routing import Router
from src.data_handlers.response import FileResponse, RedirectResponse
from settings import PUBLIC_DIR

router = Router()

router.register('/test', 'GET', lambda r: FileResponse(r, 'public/text.html'))
router.register('/redirect', 'GET', lambda r: RedirectResponse(r, '/test'))

router.use_static(PUBLIC_DIR)
