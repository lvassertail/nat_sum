
from fairseq.tasks import LegacyFairseqTask, register_task

@register_task("summarisation")
class SummarisationTask(LegacyFairseqTask):

    def __init__(self, args, src_dict, tgt_dict):
        super().__init__(args)
        self.src_dict = src_dict
        self.tgt_dict = tgt_dict

    @property
    def source_dictionary(self):
        return self.src_dict

    @property
    def target_dictionary(self):
        return self.tgt_dict