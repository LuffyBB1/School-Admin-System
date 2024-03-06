def vista_salon():
        grid_salon = SQLFORM.grid(db.salon, paginate=2)
        return dict(grid=grid_salon)
