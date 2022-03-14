class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = []

        for part in path.split("/"):
            if part == "..":
                if len(parts) > 0:
                    parts.pop()
            elif part == "" or part == ".":
                ...
            else:
                parts.append(part)

        return "/" + "/".join(parts)
