from dataclasses import dataclass


@dataclass(frozen=True)
class BTN:
    add_disable: str = 'class="btn btn-success disabled"'
    edit_disable: str = 'class="btn btn-warning disabled"'
    delete_disable: str = 'class="btn btn-danger disabled"'
    update_disable: str = 'class="btn btn-primary disabled"'
    cancel_disable: str = 'class="btn btn-secondary disabled"'
    info_disable: str = 'class="btn btn-info disabled"'

    add_tbl_disable: str = 'class="btn btn-outline-success disabled"'
    edit_tbl_disable: str = 'class="btn btn-outline-warning disabled"'
    delete_tbl_disable: str = 'class="btn btn-outline-danger disabled"'
    update_tbl_disable: str = 'class="btn btn-outline-primary disabled"'
    cancel_tbl_disable: str = 'class="btn btn-outline-secondary disabled"'
    info_tbl_disable: str = 'class="btn btn-outline-info disabled"'

    @property
    def add(self):
        return 'class="btn btn-success"'

    @property
    def edit(self):
        return 'class="btn btn-warning"'

    @property
    def delete(self):
        return 'class="btn btn-danger"'

    @property
    def update(self):
        return 'class="btn btn-primary"'

    @property
    def cancel(self):
        return 'class="btn btn-secondary"'

    @property
    def info(self):
        return 'class="btn btn-info"'

    @property
    def add_tbl(self):
        return 'class="btn btn-outline-success"'

    @property
    def edit_tbl(self):
        return 'class="btn btn-outline-warning"'

    @property
    def delete_tbl(self):
        return 'class="btn btn-outline-danger"'

    @property
    def update_tbl(self):
        return 'class="btn btn-outline-primary"'

    @property
    def cancel_tbl(self):
        return 'class="btn btn-outline-secondary"'

    @property
    def info_tbl(self):
        return 'class="btn btn-outline-info"'


class TBL:

    @property
    def model(self):
        return 'class="table  table-bordered table-hover  table-responsive" id = "TBL" '

    @property
    def head(self):
        return 'class="table-dark "'

    @property
    def body(self):
        return 'class="bg-opacity-50 bg-light"'

    @property
    def titre(self):
        return "class='h4'"
