/**
 * The knows API is defined in the parent class Relation.
 * isBadVersion(version: number): boolean {
 *     ...
 * };
 */

var solution = function(isBadVersion: any) {

    return function(n: number): number {
        var l = 0, r = n, m;
        while(l <= r){
            m = Math.floor((l + r) / 2);
            if(isBadVersion(m) && !isBadVersion(m - 1)) return m;
            else if(isBadVersion(m)) r = m - 1;
            else l = m + 1;
        }
        return l;
    };
};
