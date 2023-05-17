class ClientController:
    async def get_filters(self, filters_service: FiltersServices) -> dict: 
        markets = await filters_service.find_markets_filter()
        channels = await filters_service.find_channels_filter()
        subchannel = await filters_service.find_subchannel_filter()
        units = await filters_service.find_units_filter()

        response = {
            "unit"
        }