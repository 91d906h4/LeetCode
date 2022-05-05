/**
 * @param {number[][]} points
 * @return {number}
 */
var minTimeToVisitAllPoints = function(points) {
    var a = 0;
    for(var i = 0;i < points.length-1;i++){
        a += Math.max(Math.abs(points[i+1][0] - points[i][0]), Math.abs(points[i+1][1] - points[i][1]))
    }
    return a;
};
