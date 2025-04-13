TAVILY_API_KEY = "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"
GOOGLE_API_KEY= 'AIzaSyClTgBLxK5FR5mrV9cV765QeA4DKeLmHfs'
# Второй цикл: отправляем сообщение "whats the weather where I live?" агенту.
# Агент использует накопленную память и, возможно, инструмент поиска, чтобы сформировать ответ.
while True:
    for step in agent_executor.stream(
        {"messages": [HumanMessage(content=input())]},
        config,
        stream_mode="values",
    ):
        # Аналогично, выводим последнее сообщение из каждого шага.
        step["messages"][-1].pretty_print()