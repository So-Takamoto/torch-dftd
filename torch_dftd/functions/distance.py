from typing import Optional

import torch
from torch import Tensor


def calc_distances(
    pos: Tensor,
    edge_index: Tensor,
    cell: Optional[Tensor] = None,
    shift: Optional[Tensor] = None,
    batch_edge: Optional[Tensor] = None,
    eps=1e-20,
) -> Tensor:

    idx_i, idx_j = edge_index
    # calculate interatomic distances
    Ri = pos[idx_i]
    Rj = pos[idx_j]
    if cell is not None:
        Rj += shift
    # eps is to avoid Nan in backward when Dij = 0 with sqrt.
    Dij = torch.sqrt(torch.sum((Ri - Rj) ** 2, dim=-1) + eps)
    return Dij
