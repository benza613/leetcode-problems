class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        
        root = image[sr][sc]
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        
        q = collections.deque()
        
        """
        1. append root to q
        2. while q is not empty
        3.      pixel = popleft q, startColor = pixel
        4.      for each valid_move(startColor) for pixel: 
        5.          set m_pixel = newColor and append to q 
        
        """
        
        
        q.append((sr, sc));
        
        while q: 
            pixel = q.popleft()
            
            row, col = pixel[0], pixel[1]
            startColor = image[row][col]
            
            for move in directions: 
                
                mr, mc = row+ move[0], col+ move[1]
                
                if 0 <= mr < len(image) and 0 <= mc < len(image[0]) and image[mr][mc] == startColor and image[mr][mc] != newColor:
                    #image[mr][mc] = newColor
                    q.append((mr, mc))
                    
            image[row][col] = newColor
            print(image)
            
        return image