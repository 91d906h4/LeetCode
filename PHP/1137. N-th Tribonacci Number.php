<?php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function tribonacci($n) {
        $temp_0 = 0;
        $temp_1 = 1;
        $temp_2 = 1;
        if($n == 0){return 0;}
        else if($n == 1 || $n == 2){return 1;}
        for($i = 2;$i < $n;$i++){
            $temp_3 = $temp_0 + $temp_1 + $temp_2;
            $temp_0 = $temp_1;
            $temp_1 = $temp_2;
            $temp_2 = $temp_3;
        }
        return $temp_3;
    }
}
