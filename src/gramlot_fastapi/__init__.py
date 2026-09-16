# Copyright 2026 Softwell S.r.l. - SPDX-License-Identifier: Apache-2.0
"""Host Gramlot applications with FastAPI."""

from .application import GramlotApplication, PageCollection, mount_gramlot

__all__ = ["GramlotApplication", "PageCollection", "mount_gramlot"]
