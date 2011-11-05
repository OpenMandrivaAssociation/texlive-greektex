# revision 15878
# category Package
# catalog-ctan /fonts/greek/greektex
# catalog-date 2007-11-12 23:53:08 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-greektex
Version:	20071112
Release:	1
Summary:	Fonts for typesetting Greek/English documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/greektex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greektex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greektex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The fonts are based on Silvio Levy's classical Greek fonts;
macros and Greek hyphenation patterns for the fonts' encoding
are also provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/greektex/greektex.sty
%doc %{_texmfdistdir}/doc/latex/greektex/README
%doc %{_texmfdistdir}/doc/latex/greektex/gehyphw.gr
%doc %{_texmfdistdir}/doc/latex/greektex/greektexdoc.pdf
%doc %{_texmfdistdir}/doc/latex/greektex/greektexdoc.tex
%doc %{_texmfdistdir}/doc/latex/greektex/ywcl.zip
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
