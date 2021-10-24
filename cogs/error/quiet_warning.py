from typing import Optional


class QuietWarning(Exception):
	"""
	An error type that will be logged quietly in the log file.
	"""

	def __init__(
		self, msg: str, inner: Optional[Exception] = None,
	):
		self.inner = inner
		super().__init__(msg)
