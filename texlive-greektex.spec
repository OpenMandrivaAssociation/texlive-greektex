%global tl_name greektex
%global tl_revision 28327

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Fonts for typesetting Greek/English documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/greektex
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/greektex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/greektex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The fonts are based on Silvio Levy's classical Greek fonts; macros and
Greek hyphenation patterns for the fonts' encoding are also provided.

