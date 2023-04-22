from sqlalchemy.ext.asyncio import AsyncSession

from models.t_logs import Logs
from schemas.schemas import LogsBase

async def add_sousa_log(db: AsyncSession, request: LogsBase):
    new_log = Logs(
        program_id = request.program_id,
        user_id = request.user_id,
        message = request.message
    )
    db.add(new_log)
    await db.commit()
    await db.refresh(new_log)
    return new_log