from src.schemas.clients_schemas import FiltersResponse 

LOGGER = get_logger()

router = APIRouter(prefi="/clients", tags=["clients"])


@router.get("/filters", response_model=FiltersResponse)
async def filters(
    filters_services: FiltersServices = Depends 
    (get_filters_services),
) -> dict:
    """
    ## Return
        response_schema : {
            "markets" : 
            "subchannels" : 
        }
    """

    LOGGER.info(">> filters endpoint : mounting response")
    try:
        response = await ParametersController().get_filters(filters_services)

        return response 
    
    except Exception as error:
        LOGGER.error(f">> filters endpoint : {error}")
        raise error 