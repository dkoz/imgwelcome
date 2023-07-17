from .imgwelcome import ImgWelcome

async def setup(bot):
	n = ImgWelcome(bot)
	await bot.add_cog(n)
