import discord
from redbot.core import commands
from discord.ext import tasks
import requests
from datetime import datetime
import pytz

class Real(commands.Cog):
    """Cog for value and automatic request"""
    
    def __init__(self, bot):
        self.bot = bot
        self.auto_task_dict = {}  # Dicionário para armazenar canais e moedas configurados para envio automático
        self.auto_task.start()  # Inicia a tarefa de envio automático

    async def fetch_currency(self, currency_code):
        """Get a value consulting the API"""
        url = f"https://economia.awesomeapi.com.br/all/{currency_code}-BRL"
        try:
            response = requests.get(url)
            data = response.json()
            currency_value = data[currency_code]["bid"]  # Valor de compra
            updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return currency_value, updated_at
        except Exception:
            return None, None

    async def send_currency_embed(self, ctx, currency_code, currency_name):
        """Sends an embed with the requested currency"""
        currency_value, updated_at = await self.fetch_currency(currency_code)
        if currency_value:
            embed = discord.Embed(
                title=f"Cotação do {currency_name}",
                description=f"A cotação do {currency_name} está **R$ {currency_value}**.",
                color=discord.Color.red()
            )
            embed.add_field(name="Última atualização", value=updated_at, inline=False)
        else:
            embed = discord.Embed(
                title="Erro",
                description=f"Não foi possível obter a cotação do {currency_name}. Tente novamente mais tarde.",
                color=discord.Color.red()
            )
        await ctx.send(embed=embed)

    @commands.command(name="cotacao")
    async def fetch_currency_command(self, ctx, currency: str):
        """Command to get all currencies. Available Currencies: USD, CNY, EUR, JPY, GBP, ARS, BTC, ETH"""
        currency_map = {
            "dolar": ("USD", "Dólar"),
            "yuan": ("CNY", "Yuan Chinês"),
            "euro": ("EUR", "Euro"),
            "iene": ("JPY", "Iene Japonês"),
            "libra": ("GBP", "Libra Esterlina"),
            "peso": ("ARS", "Peso Argentino"),
            "btc": ("BTC", "Bitcoin"),
            "eth": ("ETH", "Ethereum"),
        }
        if currency.lower() in currency_map:
            currency_code, currency_name = currency_map[currency.lower()]
            await self.send_currency_embed(ctx, currency_code, currency_name)
        else:
            await ctx.send(
                "Moeda não reconhecida. Opções disponíveis: " + ", ".join(currency_map.keys())
            )

    @commands.command(name="config_auto")
    async def config_auto(self, ctx, currency_code: str, channel: discord.TextChannel):
        """Set up a channel to get the automatic updates"""
        valid_currencies = ["USD", "CNY", "EUR", "JPY", "GBP", "ARS", "BTC", "ETH"]
        if currency_code.upper() not in valid_currencies:
            await ctx.send(f"Moeda inválida. Escolha entre: {', '.join(valid_currencies)}.")
            return

        # Salva o canal e moeda configurados
        self.auto_task_dict[currency_code.upper()] = channel.id
        await ctx.send(f"Envio automático de {currency_code.upper()} configurado para o canal {channel.mention}.")

    @tasks.loop(hours=24)
    async def auto_task(self):
        """Automatically sends updates"""
        for currency_code, channel_id in self.auto_task_dict.items():
            channel = self.bot.get_channel(channel_id)
            if channel:
                currency_value, updated_at = await self.fetch_currency(currency_code)
                if currency_value:
                    await channel.send(f"A cotação de {currency_code} é **R$ {currency_value}** (Atualizado em {updated_at}).")
                else:
                    await channel.send(f"Erro ao obter a cotação de {currency_code}.")

    @auto_task.before_loop
    async def before_auto_task(self):
        """Wait until the correct time to send the updates"""
        utc_now = datetime.now(pytz.utc)
        sao_paulo_tz = pytz.timezone("America/Sao_Paulo")
        local_time = utc_now.astimezone(sao_paulo_tz)
        target_time = local_time.replace(hour=12, minute=0, second=0, microsecond=0)

        if local_time > target_time:
            target_time = target_time.replace(day=local_time.day + 1)

        await discord.utils.sleep_until(target_time)

def setup(bot):
    """Set up the cog on the bot"""
    bot.add_cog(Real(bot))
