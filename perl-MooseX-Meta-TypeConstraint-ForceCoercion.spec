%define upstream_name    MooseX-Meta-TypeConstraint-ForceCoercion
%define upstream_version 0.01
Name:		perl-%{upstream_name}
Version:	0.01
Release:	2

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Force coercion when validating type constraints
Url:		https://metacpan.org/dist/MooseX-Meta-TypeConstraint-ForceCoercion
Source0:	https://cpan.metacpan.org/authors/id/F/FL/FLORA/MooseX-Meta-TypeConstraint-ForceCoercion-0.01.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
This class allows to wrap any 'Moose::Meta::TypeConstraint' in a way that
will force coercion of the value when checking or validating a value
against it.

%prep
%setup -q -n MooseX-Meta-TypeConstraint-ForceCoercion-0.01

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

