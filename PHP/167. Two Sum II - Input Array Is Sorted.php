class Solution {

    /**
     * @param Integer[] $numbers
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($numbers, $target) {
        $a = count($numbers) - 1;
        $b = 0;
        while($numbers[$a] + $numbers[$b] != $target){
            if($numbers[$a] + $numbers[$b] > $target){ $a--; }
            else{ $b ++; }
        }
        return [$b + 1, $a + 1];
    }
}
