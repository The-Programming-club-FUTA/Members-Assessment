def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    def dfs(image: List[List[int]], r: int, c: int, color: int, new_color: int):
        if image[r][c] == color:
            image[r][c] = new_color
            if r >= 1:
                dfs(image, r - 1, c, color, new_color)
            if c >= 1:
                dfs(image, r, c - 1, color, new_color)
            if r + 1 < len(image):
                dfs(image, r + 1, c, color, new_color)
            if c + 1 < len(image[0]):
                dfs(image, r, c, color, new_color)


    old_color = image[sr][sc]
    if old_color != color:
        dfs(image, sr, sc, color, color)

    return image