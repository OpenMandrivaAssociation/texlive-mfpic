# revision 28444
# category Package
# catalog-ctan /graphics/mfpic
# catalog-date 2012-12-04 16:44:12 +0100
# catalog-license lppl1.3
# catalog-version 1.10
Name:		texlive-mfpic
Version:	1.10
Release:	9
Summary:	Draw Metafont/post pictures from (La)TeX commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/mfpic
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mfpic.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mfpic.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mfpic.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Mfpic is a scheme for producing pictures from (La)TeX commands.
Commands \mfpic and \endmfpic (in LaTeX, the mfpic environment)
enclose a group in which drawing commands may be placed. The
commands generate a Meta-language file, which may be processed
by Metapost (or even Metafont). The resulting image file will
be read back in to the document to place the picture at the
point where the original (La)TeX commands appeared. Note that
the ability to use Metapost here means that the package works
equally well in LaTeX and PDFLaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metafont/mfpic/grafbase.mf
%{_texmfdistdir}/metapost/mfpic/dvipsnam.mp
%{_texmfdistdir}/metapost/mfpic/grafbase.mp
%{_texmfdistdir}/tex/generic/mfpic/mfpic.sty
%{_texmfdistdir}/tex/generic/mfpic/mfpic.tex
%{_texmfdistdir}/tex/generic/mfpic/mfpicdef.tex
%doc %{_texmfdistdir}/doc/generic/mfpic/README
%doc %{_texmfdistdir}/doc/generic/mfpic/changes.txt
%doc %{_texmfdistdir}/doc/generic/mfpic/coil.mps
%doc %{_texmfdistdir}/doc/generic/mfpic/examples/data.dat
%doc %{_texmfdistdir}/doc/generic/mfpic/examples/forfun.tex
%doc %{_texmfdistdir}/doc/generic/mfpic/examples/lapictures.tex
%doc %{_texmfdistdir}/doc/generic/mfpic/examples/pictures.tex
%doc %{_texmfdistdir}/doc/generic/mfpic/install.txt
%doc %{_texmfdistdir}/doc/generic/mfpic/lcheadings.ist
%doc %{_texmfdistdir}/doc/generic/mfpic/mfpcard.pdf
%doc %{_texmfdistdir}/doc/generic/mfpic/mfpcard.tex
%doc %{_texmfdistdir}/doc/generic/mfpic/mfpdoc.sty
%doc %{_texmfdistdir}/doc/generic/mfpic/mfpguide.pdf
%doc %{_texmfdistdir}/doc/generic/mfpic/mfpguide.tex
%doc %{_texmfdistdir}/doc/generic/mfpic/mfpic-doc.pdf
%doc %{_texmfdistdir}/doc/generic/mfpic/mfpic-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/mfpic/grafbase.dtx
%doc %{_texmfdistdir}/source/generic/mfpic/mfpic.dtx
%doc %{_texmfdistdir}/source/generic/mfpic/mfpic.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metafont metapost tex doc source %{buildroot}%{_texmfdistdir}
