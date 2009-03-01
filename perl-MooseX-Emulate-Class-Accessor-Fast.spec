#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MooseX
%define	pnam	Emulate-Class-Accessor-Fast
Summary:	MooseX::Adopt::Class::Accessor::Fast - Hijack Class::Accessor::Fast in %INC
#Summary(pl.UTF-8):	
Name:		perl-MooseX-Emulate-Class-Accessor-Fast
Version:	0.00800
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	050c85f8f30584bcfafe4f96af4d9ef0
URL:		http://search.cpan.org/dist/MooseX-Emulate-Class-Accessor-Fast/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Moose >= 0.31
BuildRequires:	perl-namespace-clean
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module attempts to hijack Class::Accessor::Fast in %INC and
replace it with MooseX::Emulate::Class::Accessor::Fast. Make sure it is
loaded before the classes you have that use <Class::Accessor::Fast>. It
is meant as a tool to help you migrate your project from
Class::Accessor::Fast, to MooseX::Emulate::Class::Accessor::Fast and
ultimately, to Moose.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/MooseX/Adopt
%{perl_vendorlib}/MooseX/Emulate
%{_mandir}/man3/*
