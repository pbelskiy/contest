class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for path in paths:
            root, *files = path.split(' ')

            for file in files:
                name, content = file.split('(')
                d[content].append(os.path.join(root, name))

        return filter(lambda v: len(v) > 1, d.values())
