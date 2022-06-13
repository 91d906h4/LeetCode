class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function buildArray($nums) {
        foreach($nums as $i){
            $result[] = $nums[$i];
        }
        return $result;
    }
}
