class TextEditor:

    def __init__(self):
        self.data = ''
        self.cursor = 0

    def addText(self, text: str) -> None:
        before, after = self.data[:self.cursor], self.data[self.cursor:]
        self.data = before + text + after
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        before, after = self.data[:self.cursor], self.data[self.cursor:]

        deleted = len(before)
        before = before[:-k]
        deleted -= len(before)

        self.data = before + after
        self.cursor -= deleted
        return deleted

    def cursorLeft(self, k: int) -> str:
        self.cursor -= min(self.cursor, k)
        return self.data[self.cursor - min(10, self.cursor):self.cursor]

    def cursorRight(self, k: int) -> str:
        _max = len(self.data) - self.cursor
        self.cursor += min(k, _max)
        return self.data[self.cursor - min(10, self.cursor):self.cursor]
