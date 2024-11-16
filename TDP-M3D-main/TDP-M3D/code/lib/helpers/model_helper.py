from lib.models.TDP-M3D import TDP-M3D


def build_model(cfg,mean_size):
    if cfg['type'] == 'TDP-M3D':
        return TDP-M3D(backbone=cfg['backbone'], neck=cfg['neck'], mean_size=mean_size)
    else:
        raise NotImplementedError("%s model is not supported" % cfg['type'])
