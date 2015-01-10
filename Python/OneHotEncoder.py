from scipy import sparse


class OneHotEncoder():
    """
    OneHotEncoder takes data matrix with categorical columns and
    converts it to a sparse binary matrix doing one-of-k encoding.

    Parts of code borrowed from Paul Duan (www.paulduan.com)
    Licence: MIT (https://github.com/pyduan/amazonaccess/blob/master/MIT-LICENSE)
    """

    def __init__(self):
        self.keymap = None

    def fit(self, x):
        self.keymap = []
        for col in x.T:
            uniques = set(list(col))
            self.keymap.append(dict((key, i) for i, key in enumerate(uniques)))

    def partial_fit(self, x):
        """
        This method can be used for doing one hot encoding in mini-batch mode.
        """
        if self.keymap is None:
            self.fit(x)
        else:
            for i, col in enumerate(x.T):
                uniques = set(self.keymap[i].keys() + (list(col)))
                self.keymap[i] = dict((key, i) for i, key in enumerate(uniques))

    def transform(self, x):
        if self.keymap is None:
            self.fit(x)

        outdat = []
        for i, col in enumerate(x.T):
            km = self.keymap[i]
            num_labels = len(km)
            spmat = sparse.lil_matrix((x.shape[0], num_labels))
            for j, val in enumerate(col):
                if val in km:
                    spmat[j, km[val]] = 1
            outdat.append(spmat)
        outdat = sparse.hstack(outdat).tocsr()
        return outdat