# import os
# import pwd
# from sys import stderr

# from loguru import logger

# username = pwd.getpwuid(os.geteuid()).pw_name


# logger.remove()

# logger.add(
#    sink=stderr, format="{time} <r>{level}</r> <g>{message}</g> {file}", level="INFO"
# )

# logger.add(
#    "meu_arquivo_de_logs.log", format="{time} {level} {message} {file}", level="INFO"
# )


# logger.add("meu_log.log",level="CRITICAL")
# def soma(x, y):
#    try:
#        soma = x + y
#        logger.info(f"você digitou os números corretos parabéns {soma}")
#    except soma.DoesNotExist:
#        logger.critical("você tem que digitar os valores corretos")


# print(soma("3", 5))
