class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        created = set()
        supplies = set(supplies)
        used = set()

        new = True

        while new:
            new = False

            for i in range(len(recipes)):
                if i in used:
                    continue

                if set(ingredients[i]).issubset(supplies | created):
                    used.add(i)
                    created.add(recipes[i])
                    new = True

        return list(created)
