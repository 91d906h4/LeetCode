<?php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[]
     */
    function twoSum($nums, $target) {
        $arr = array();

        for ($i = 0; $i < count($nums); $i++) {
            if (in_array($target - $nums[$i], $arr))
                return array($i, array_search($target - $nums[$i], $arr));
            
            $arr[$i] = $nums[$i];
        }

        return array(0, 0);
    }
}
