
os.environ["TAVILY_API_KEY"] =keys.TAVILY_API_KEY
os.environ["GOOGLE_API_KEY"] = keys.GOOGLE_API_KEY
# Создаём экземпляр генеративной модели ИИ от Google, используя модель "gemini-2.0-flash"
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Инициализируем объект для сохранения состояния диалога (память агента)
memory = MemorySaver()

# Создаём объект инструмента для поиска, ограничивая число результатов до 2
search = TavilySearchResults(max_results=2)

# Собираем все инструменты в список. Здесь используется только инструмент поиска.
tools = [search]

# Создаём агента, который будет обрабатывать запросы.
# Для этого передаём ему генеративную модель, список инструментов и объект для сохранения памяти.
agent_executor = create_react_agent(llm, tools, checkpointer=memory)
f# Создаём конфигурационный словарь с настройками, например, идентификатором потока.
config = {"configurable": {"thread_id": "abc123"}}

# Первый цикл: отправляем сообщение "hi im bob! and i live in berlin" агенту и выводим промежуточные шаги выполнения.

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