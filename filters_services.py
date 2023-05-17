async def find_markets_filter(self) -> list:
    try:
        stmt = (
            select(CanalSubcanalMercado.id_mercado, CanalSubcanalMercado.mercado)
            .group_by(CanalSubcanalMercado.id_mercado, CanalSubcanalMarcedo.mercado)
            .order_by(asc(CanalSubcanalMercado.id_mercado))
        )
        

        result = (await self.db.execute(stmt)).all()

        if not result:
            raise ValueNotFoundInDBError
        
        return result 
    
    except Exception as error:
        LOGGER.error(f">> find_markets_filter function : {error}")
        raise error 
    

async def find_subchannel_filter(self) -> list:
    try:
        stmt = (
            select(CanalSubcanalMercado.id_subcanal, CanalSubcanalMercado.subcanal)
            .group_by(CanalSubcanalMercado.id_subcanal, CanalSubcanalMarcedo.subcanal)
            .order_by(asc(CanalSubcanalMercado.id_subcanal))
        )
        

        result = (await self.db.execute(stmt)).all()

        if not result:
            raise ValueNotFoundInDBError
        
        return result 
    
    except Exception as error:
        LOGGER.error(f">> find_markets_filter function : {error}")
        raise error 