class Solution {
    /**
     * @param String $s
     * @param Integer[] $indices
     * @return String
     */
    function restoreString($s, $indices) {
        $r = $s;

        for ($i = 0 ; $i < strlen($s) ; $i++ ) {
            $r[$indices[$i]] = $s[$i];
        }

        return $r;
    }
}


