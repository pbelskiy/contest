import "math"

func maxArea(height []int) int {
    max := 0
    left := 0
    right := len(height) - 1
    
    for left < right {
        square := (right - left) * int(math.Min(float64(height[left]), float64(height[right])))
        
        if square > max {
            max = square
        }
        
        if (height[left] > height[right]) {
            right--
        } else {
            left++
        }
    }
    
    return max
}


