class BTN:

    @property
    def add(self):
        return 'class="btn btn-success"'

    @property
    def edit(self):
        return 'class="btn btn-warning"'

    @property
    def remove(self):
        return 'class="btn btn-danger"'

    @property
    def update(self):
        return 'class="btn btn-primary"'

    @property
    def cancel(self):
        return 'class="btn btn-secondary"'

    @property
    def add_tbl(self):
        return 'class="btn btn-outline-success"'

    @property
    def edit_tbl(self):
        return 'class="btn btn-outline-warning"'

    @property
    def remove_tbl(self):
        return 'class="btn btn-outline-danger"'

    @property
    def update_tbl(self):
        return 'class="btn btn-outline-primary"'

    @property
    def cancel_tbl(self):
        return 'class="btn btn-outline-secondary"'


class TBL:

    @property
    def model(self):
        return 'class="table  table-bordered table-hover  table-responsive-sm"'

    @property
    def head(self):
        return 'class="table-dark "'

    @property
    def body(self):
        return 'class="bg-opacity-50 bg-light"'

    @property
    def titre(self):
        return "class='h4'"
