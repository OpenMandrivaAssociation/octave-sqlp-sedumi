%global octpkg sqlp-sedumi

Summary:	SeDuMi (Self-Dual-Minimization) is solving convex optimization problems for Octave
Name:		octave-sqlp-sedumi
Version:	1.3.5
Release:	2
License:	GPLv2+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/sqlp-sedumi/
Url:		https://github.com/sqlp/sedumi/
Source0:	https://github.com/sqlp/sedumi/archive/v%{version}/sqlp-sedumi-%{version}.tar.gz

BuildRequires:  octave-devel >= 4.0.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
SeDuMi (Self-Dual-Minimization) is solving convex optimization
problems involving linear equations and inequalities, second-order
cone constraints, and semidefinite constraints (linear matrix
inequalities).

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n sedumi-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

