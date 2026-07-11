%global tl_name mfpic
%global tl_revision 28444

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.10
Release:	%{tl_revision}.1
Summary:	Draw Metafont/post pictures from (La)TeX commands
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/mfpic
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mfpic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mfpic.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mfpic.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Mfpic is a scheme for producing pictures from (La)TeX commands. Commands
\mfpic and \endmfpic (in LaTeX, the mfpic environment) enclose a group
in which drawing commands may be placed. The commands generate a Meta-
language file, which may be processed by MetaPost (or even Metafont).
The resulting image file will be read back in to the document to place
the picture at the point where the original (La)TeX commands appeared.
Note that the ability to use MetaPost here means that the package works
equally well in LaTeX and pdfLaTeX.

