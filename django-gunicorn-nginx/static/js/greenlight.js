(function () {
    "use strict";
    function enlarge() {
        document.getElementById("changeme").style.color = "green";
        document.getElementById("changeme").style.fontSize = "xx-large";
        return false;
    }
    document.getElementById("changeme").addEventListener("mouseover", enlarge);
}());
