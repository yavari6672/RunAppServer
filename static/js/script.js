function TBL_Auto(checkbox) {
    if (!checkbox.checked) {
        document.getElementById("TBL").className = "table  table-bordered table-hover  table-responsive"
    } else {
        document.getElementById("TBL").className = "table  table-bordered table-hover  table-responsive text-nowrap"
    }
}