import discord
from redbot.core import commands
from discord.ext import tasks
import requests
from datetime import datetime
import pytz

class Real(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.auto_task_dict = {}  # Dicionário para armazenar os canais de envio automático por moeda
        # Removido o start da tarefa dolar_task
        self.auto_task.start()  # Inicia a tarefa de envio automático para as moedas configuradas

    async def fetch_currency(self, currency_code):
        """Função genérica para obter a cotação de qualquer moeda"""
        url = f"https://economia.awesomeapi.com.br/all/{currency_code}-BRL"
        try:
            response = requests.get(url)
            data = response.json()
            currency_value = data[currency_code]["bid"]  # Valor da compra
            updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return currency_value, updated_at
        except Exception as e:
            return None, None

    @commands.command(name="dolar")
    async def fetch_dolar(self, ctx):
        """Comando que envia a cotação do dólar"""
        currency_value, updated_at = await self.fetch_currency("USD")
        if currency_value:
            embed = discord.Embed(
                title="Cotação do Dólar",
                description=f"A cotação do dólar está **R$ {currency_value}**.",
                color=discord.Color.red()  # Cor vermelha
            )
            embed.add_field(name="Última atualização", value=updated_at, inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Erro",
                description="Não foi possível obter a cotação do dólar. Tente novamente mais tarde.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

    @commands.command(name="yuan")
    async def fetch_yuan(self, ctx):
        """Comando que envia a cotação do yuan"""
        currency_value, updated_at = await self.fetch_currency("CNY")
        if currency_value:
            embed = discord.Embed(
                title="Cotação do Yuan Chinês",
                description=f"A cotação do Yuan Chinês está **R$ {currency_value}**.",
                color=discord.Color.red()
            )
            embed.add_field(name="Última atualização", value=updated_at, inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Erro",
                description="Não foi possível obter a cotação do Yuan. Tente novamente mais tarde.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

    @commands.command(name="euro")
    async def fetch_euro(self, ctx):
        """Comando que envia a cotação do Euro"""
        currency_value, updated_at = await self.fetch_currency("EUR")
        if currency_value:
            embed = discord.Embed(
                title="Cotação do Euro",
                description=f"A cotação do Euro está **R$ {currency_value}**.",
                color=discord.Color.red()
            )
            embed.add_field(name="Última atualização", value=updated_at, inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Erro",
                description="Não foi possível obter a cotação do Euro. Tente novamente mais tarde.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

    @commands.command(name="iene")
    async def fetch_iene(self, ctx):
        """Comando que envia a cotação do Iene Japonês"""
        currency_value, updated_at = await self.fetch_currency("JPY")
        if currency_value:
            embed = discord.Embed(
                title="Cotação do Iene Japonês",
                description=f"A cotação do Iene Japonês está **R$ {currency_value}**.",
                color=discord.Color.red()
            )
            embed.add_field(name="Última atualização", value=updated_at, inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Erro",
                description="Não foi possível obter a cotação do Iene. Tente novamente mais tarde.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

    @commands.command(name="libra")
    async def fetch_gbp(self, ctx):
        """Comando que envia a cotação da Libra Esterlina"""
        currency_value, updated_at = await self.fetch_currency("GBP")
        if currency_value:
            embed = discord.Embed(
                title="Cotação da Libra Esterlina",
                description=f"A cotação da Libra Esterlina está **R$ {currency_value}**.",
                color=discord.Color.red()
            )
            embed.add_field(name="Última atualização", value=updated_at, inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Erro",
                description="Não foi possível obter a cotação da Libra Esterlina. Tente novamente mais tarde.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

    @commands.command(name="peso")
    async def fetch_peso(self, ctx):
        """Comando que envia a cotação do Peso Argentino"""
        currency_value, updated_at = await self.fetch_currency("ARS")
        if currency_value:
            embed = discord.Embed(
                title="Cotação do Peso Argentino",
                description=f"A cotação do Peso Argentino está **R$ {currency_value}**.",
                color=discord.Color.red()
            )
            embed.add_field(name="Última atualização", value=updated_at, inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Erro",
                description="Não foi possível obter a cotação do Peso Argentino. Tente novamente mais tarde.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

    @commands.command(name="btc")
    async def fetch_btc(self, ctx):
        """Comando que envia a cotação do Bitcoin"""
        currency_value, updated_at = await self.fetch_currency("BTC")
        if currency_value:
            embed = discord.Embed(
                title="Cotação do Bitcoin",
                description=f"A cotação do Bitcoin está **R$ {currency_value}**.",
                color=discord.Color.red()
            )
            embed.add_field(name="Última atualização", value=updated_at, inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Erro",
                description="Não foi possível obter a cotação do Bitcoin. Tente novamente mais tarde.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

    @commands.command(name="eth")
    async def fetch_eth(self, ctx):
        """Comando que envia a cotação do Ethereum"""
        currency_value, updated_at = await self.fetch_currency("ETH")
        if currency_value:
            embed = discord.Embed(
                title="Cotação do Ethereum",
                description=f"A cotação do Ethereum está **R$ {currency_value}**.",
                color=discord.Color.red()
            )
            embed.add_field(name="Última atualização", value=updated_at, inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title="Erro",
                description="Não foi possível obter a cotação do Ethereum. Tente novamente mais tarde.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)

    @commands.command(name="config_auto")
    async def config_auto(self, ctx, currency_code: str, channel: discord.TextChannel):
        """Configura o canal para enviar a cotação de uma moeda automaticamente"""
        if currency_code not in ["USD", "CNY", "EUR", "JPY", "GBP", "ARS", "BTC", "ETH"]:
            await ctx.send("Código de moeda inválido. Use um dos seguintes: USD, CNY, EUR, JPY, GBP, ARS, BTC, ETH.")
            return
        
        # Armazenando o canal e a moeda para envio automático
        self.auto_task_dict[currency_code] = channel.id
        await ctx.send(f"Envio automático da cotação de {currency_code} configurado para o canal {channel.mention}.")

    @tasks.loop(hours=24)
    async def auto_task(self):
        """Envia as cotações automáticas para os canais configurados"""
        utc_now = datetime.now(pytz.utc)
        utc_offset = pytz.timezone("America/Sao_Paulo")
        local_time = utc_now.astimezone(utc_offset)

        # Se for às 12:00
        if local_time.hour == 12 and local_time.minute == 0:
            for currency_code, channel_id in self.auto_task_dict.items():
                channel = self.bot.get_channel(channel_id)
                if channel:
                    currency_value, updated_at = await self.fetch_currency(currency_code)
                    if currency_value:
                        await channel.send(f"A cotação de {currency_code} está R$ {currency_value}.")
                    else:
                        await channel.send(f"Não foi possível obter a cotação de {currency_code}. Tente novamente mais tarde.")
    
    @auto_task.before_loop
    async def before_auto_task(self):
        """Espera até o horário da primeira execução do loop (12:00 UTC-3)"""
        utc_now = datetime.now(pytz.utc)
        utc_offset = pytz.timezone("America/Sao_Paulo")
        local_time = utc_now.astimezone(utc_offset)
        target_time = local_time.replace(hour=12, minute=0, second=0, microsecond=0)

        if local_time > target_time:
            target_time = target_time.replace(day=local_time.day + 1)

        wait_seconds = (target_time - local_time).total_seconds()
        await discord.utils.sleep_until(target_time)

def setup(bot):
    bot.add_cog(Real(bot))
