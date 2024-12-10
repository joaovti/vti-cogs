from .real import Real


async def setup(bot):
    await bot.add_cog(Real(bot))
