def train():
    model.forward()
    model.backward()
    lr.step()
